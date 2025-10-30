import os
import dotenv
from decimal import Decimal
from django.conf import settings
from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from .models import Car, CarInventory
from gemini_api.client import get_car_ai_bio_gemini

dotenv.load_dotenv()


# ============================================================
# Atualiza o inventário de carros (contagem e soma dos preços)
# ============================================================
def car_inventory_update():
    cars_count = Car.objects.count()

    total_price = Car.objects.aggregate(
        total_price=Sum('price')
    )['total_price'] or Decimal('0.00')

    # Divide por 10 para salvar o valor em "milhares de reais"
    adjusted_price = total_price / Decimal('10')

    CarInventory.objects.create(
        cars_count=cars_count,
        cars_price=adjusted_price
    )


# ============================================================
# Preenche a bio automaticamente com IA, se estiver vazia
# ============================================================
@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        try:
            bio = get_car_ai_bio_gemini(instance.model, instance.brand, instance.factory_year)
            # Se a API retornar erro formatado, ignora
            if "error" in str(bio).lower():
                instance.bio = None
            else:
                instance.bio = bio
        except Exception as e:
            # Garante que não quebre o save
            instance.bio = None


# ============================================================
# Atualiza o inventário após salvar ou deletar
# ============================================================
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, created, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()


# ============================================================
# Limpeza de fotos antigas (nova parte)
# ============================================================
@receiver(pre_save, sender=Car)
def delete_old_photo_on_change(sender, instance, **kwargs):
    """Remove a imagem antiga se for trocada por uma nova."""
    if not instance.pk:
        return  # novo objeto, nada a apagar

    try:
        old_car = Car.objects.get(pk=instance.pk)
    except Car.DoesNotExist:
        return

    old_photo = old_car.photo
    new_photo = instance.photo

    if old_photo and old_photo != new_photo:
        old_path = os.path.join(settings.MEDIA_ROOT, old_photo.name)
        if os.path.isfile(old_path):
            os.remove(old_path)


@receiver(post_delete, sender=Car)
def delete_photo_on_delete(sender, instance, **kwargs):
    """Apaga a imagem do disco ao deletar o carro."""
    if instance.photo:
        photo_path = os.path.join(settings.MEDIA_ROOT, instance.photo.name)
        if os.path.isfile(photo_path):
            os.remove(photo_path)
