customers = Customers.objects.all()

firstCustomer = Customers.objects.first()

lastCustomer = Customers.objects.last()

customerByName = Customers.objects.get(name='Peter Piper')

customerById = Customers.objects.get(id=4)

firstCustomer.order_set.all()

order = Order.objects.first()
parentName = Order.customer.name

products = Product.objects.filter(category="Out Door")

leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

productsFiltered = Product.objects.filter(tags_name="Sports")

ballOrders = firstCustomer.order_set.filter(products__name="Ball").count()

allOrders = {}

for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1


class ParentModel(models.Model):
    name = models.CharField(max_lenth=200, null=True)

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_lenth=200, null=True)

parent = ParentModel.objects.first()
parent.ChildModel_set.all()
