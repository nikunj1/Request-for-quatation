from openerp.osv import  osv,fields
from datetime import datetime 
from _smbc import Context

class request_quatation(osv.osv):
    _name = 'rfq.order'
    
    
    _columns = {
                 'order_date' : fields.datetime("Order date"),
                 'schedule_date' : fields.datetime("Schedule Date"),
                 'order_line': fields.one2many('order.line', 'order_id', 'Order Lines'),
                
                }
    

class order_lines(osv.osv):
    _name = 'order.line'
  
    _columns ={
               'product_qty': fields.float('Quantity'),
               'name' : fields.many2one('res.partner', 'Supplier',  domain = [('supplier','=',True)], help="Supplier of this product"),
               'product_id': fields.many2one('product.product','Product' ),
               'order_id': fields.many2one('rfq.order', 'Order Id')
              }
    _defaults = {
        
        'product_qty': 1.0,
        
    }
    def onchange_lamp_type_id(self, cr, uid,  ids, product_id, context=None):
        list = []
        res = {}
        domain = {}
        if product_id == False:
            return {}
        print "_______----------", product_id
        obj_product = self.pool.get('product.product')
        
        fetch_product = obj_product.browse(cr,uid,product_id)
        list_ids = fetch_product.seller_ids
        obj_price = self.pool.get('pricelist.partnerinfo')  
        fetch_price = obj_price.browse(cr,uid,product_id)
        print fetch_price
        print"__________________________"
#         for id in list_ids:
#             list_name = [id.name.name]
#             print list_name 
#             su = id.name
#              
#              
#             # res = {'domain':domain}
#               
#             print su
#             #  res = {'domain': { 'name':[('name','in',list_name)]}}
#             domain = { 'name':[('name','in',list_name)]}
#             print "domain"
#             print domain
#             list = [domain]
#             print "----------"
#               
#             res['domain'] =  domain
#             list = [res]
#             print list
#             print res 
#         # res = {'value': domain,'domain':domain,'warning':'Warning Message'}\
#         print "test"
#         print list
#         print "res"
#         print res
        
        list = []
        for id in list_ids:
            list.append(id.name.id)
        res['domain'] = {'name' : [('id', 'in',list)]}
        print res
        return res
class res_partner(osv.osv):
    _inherit = 'res.partner'
    
    def name_get(self, cr, user, ids, context=None):
         if context is None:
             context ={}
         if isinstance(ids, (int, long)):
            ids = [ids]
         if not len(ids):
            return []

         def _name_get(d):
             name = d.get('name','')
             print "_____________"
             print name
             code = d.get('price',False) or False
             if code:
                 name = '[%s] %s' % (code,name)
                 print "-------------------------------"
                 print "name"
                 print name
             return (d['id'], name)
         
        
         result = []
         print context
        
         
         product_id = context.get('product_id', False)
         if product_id:
             mydict = {}
             print "partnert"
             print product_id
             obj_product = self.pool.get('product.product')
             fetch_product = obj_product.browse(cr,user,product_id,context=context)
             list_ids = fetch_product.seller_ids
             print "listIDDDDDDDDDDDD"
             print list_ids
             for p_id in list_ids:
                 print "list"
                 print p_id.name
                 print p_id.pricelist_ids
                 print "empty"
                 for unit_id in p_id.pricelist_ids:
                     print "unit_id"
                     print p_id.name.name
                     print unit_id.price
                     print "unit price"
                  #  id.name.name
                     print "list name"
                     if unit_id.price:
                         mydict = {
                                 'id': p_id.name.id,
                                 'name' : p_id.name.name,
                                 'price': unit_id.price
                                 }
                     
                         print "result" 
                         print mydict
         
                     else:
                         mydict = {
                                 'id': p_id.name.id,
                                 'name' : p_id.name.name,
                                
                                 }
                     
                         print "result" 
                         print mydict
                         result.append(_name_get(mydict))
         
         else:
            return super(res_partner, self).name_get(cr, user, ids, context=context)
         print "------"
         print result
         print "-------"
         return result
 
  
    def name_search(self, cr, user, name='', args=None, operator='ilike', context=None, limit=100):
         print "------------"
         ids = self.search(cr, user, args, limit=limit, context=context)
         print "ids__________________________"
         print ids
         result = self.name_get(cr, user, ids, context=context)
         print "result __________________________"
         print result
         print "complete----------------------------------"
         return result
            