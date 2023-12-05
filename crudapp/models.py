from django.db import models

class PlacementDetails(models.Model):
    placement_id = models.BigAutoField(primary_key=True)
    work_order_no = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    candidate_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100, blank=True, null=True)
    pay_type = models.CharField(max_length=100, blank=True, null=True)
    business_unit = models.CharField(max_length=100, blank=True, null=True)
    work_site = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    bill_rate = models.FloatField()
    pay_rate = models.FloatField(blank=True, null=True)
    bill_rate_after_msp = models.CharField(max_length=100, blank=True, null=True)
    vendor_name = models.CharField(max_length=100, blank=True, null=True)
    markup = models.CharField(max_length=100, blank=True, null=True)
    ot_pay_rate_per_hour = models.FloatField(blank=True, null=True)
    ot_bill_rate_per_hour = models.FloatField(blank=True, null=True)
    dt_pay_rate_per_hour = models.FloatField(blank=True, null=True)
    dt_bill_rate_per_hour = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    job_id = models.CharField(max_length=100)
    hired_no = models.CharField(max_length=100, blank=True, null=True)
    startend_date = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'placement_details'

# Create your models here.
