from openerp.osv import  osv,fields
from datetime import datetime 




   
class rfq(osv.osv):
    _name = 'rfq.order'
   
    _columns = {
                    'order_date' : fields.datetime("Order date"),
                    'schedule_date' : fields.datetime("Schedule Date"),
                   
                    'order_line': fields.one2many('order.line', 'order_id', 'Order Lines'),
                   
                    
                }
class supplyer(osv.osv):
    _name = 'supplyer.info'
    _rec_name="supplyer_id"
    
    _columns ={
               'supplyer_id' : fields.char("Supplyer Name"),
               
              
               'order_id': fields.many2one('rfq.order', 'Order Lines')
              
               }
class product(osv.osv):
    _name = 'product.order'
    _rec_name="product"
    
    _columns = {
                     'product' : fields.char("Product")
                }
class order_line(osv.osv):
    _name = 'order.line'
    
    _columns = {
                 'supplyer_id' : fields.many2one("supplyer.info","Supplyer"),
                 'product_id'   : fields.many2one("product.order","Product"),
                 'order_id': fields.many2one('rfq.order', 'Order Lines'),
                 'quantity' : fields.integer("Quantity")
                }