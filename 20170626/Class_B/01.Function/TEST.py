e#1. 입력 값, 리턴 값이 있는 함수
#   리턴 값 받을 변수 = 함수명(입력인수, ...)
#
#def sum(a, b):
#     result = a + b
#     return result
#
#a = sum(3, 4)
#print (a)  
#
#==================================================================
#
#2. 입력 값은 있고, 리턴 값이 없는 함수
#   함수명(입력인수, ...)
#def sum(a, b):
#     print "%d, %d의 합은 %d입니다." % (a, b, a+b) 
#
#a = sum(3, 4)
#print a
#
#===================================================================
#
#
#===================================================================
#
#3. 입력 값 없고, 리턴 값이 있는 함수
#   리턴 값 받을 변수 = 함수명()
#def say():
#     return ('Hi')
#
#a = say()
#print (a)
#
#===================================================================
#
#4. 입력값도 리턴값도 없는 함수
#def say():
#     print ('Hi')
#
#say()
#print a
#
#===================================================================
#
#5. 다수의 입력 값을 받는 함수
#
#def summany(*args):
#    sum = 0
#    for i in args:
#        sum = sum + i
#    return sum  
#
#*args 는 관례적 표현 '*'만 붙이면 됩
#
#result = summany(1,2,3)
#print (result)  
#
#result = sum_many(1,2,3,4,5)
#print result  

#===================================================================
# 
#def sum_mul(choice,*args):
#  if choice == "sum":
#    result=0
#    for i in args:
#      result = result + i
#  elif choice == "mul":
#    result=1
#    for i in args:
#      result=result*i
#  return result

#===================================================================
# 
#def sum_mul(choice,**kwargs):
#  if choice == "sum":
#    result=0
#   if kwargs.get('mul') == 'true':
#     result =0
#  return result

a = sum_mul('none', {'mul':'true'})
#===================================================================
#def sum_and_mul(a,b):
#  return a+b
#  return a*b
#  
#a = sum_and_mul(3,4)  
#print (a)
#


#s,m = sum_and_mul(3,4)
#print (s)
#print (m)


#===================================================================
# return 으로 빠져나가기

#def say_nick(nick):
#    if nick=="바보":
#      return
#    print("나의 별명은 %s 입니다.") %nick
#    
#say_nick("바보")
#

#===================================================================
# 초기값 설정

#def say_myself(name,old,sex=1):
#  print("나의 이름은 %s 입니다.") %name
#  print("나이는 %d 살입니다.") %old
#  if sex:
#    print("남자입니다.")
#  else:
#    print("여자입니다.")
#    
#    
#say_myself("박응용",27,1)

#===================================================================
#
# 함수내 선언된 변수의 효력 범위
# a=1 

# def vartest(a):
#   a=a+1
# vartest(a)
# print(a)



# a=1

# def vartest(a):
#   a=a+1
#   return a
  
# a=vartest(a)
# print(a)



================================

def _get_instances_by_filters_all_cells(self, context, *args, **kwargs):
        """This is just a wrapper that iterates (non-zero) cells."""
        load_cells()
        if len(CELLS) == 1:
            # We always expect at least two cells; one for cell0 and one for at
            # least a single main cell. If there is only one cell it indicates
            # that nova-api was started before all of the cells were mapped and
            # we should provide a warning to the operator.
            LOG.warning('At least two cells are expected but only one '
                        'was found (%s). cell0 and the initial main cell '
                        'should be created before starting nova-api since '
                        'the cells are cached in each worker. When you '
                        'create more cells, you will need to restart the '
                        'nova-api service to reset the cache.',
                        CELLS[0].identity)

        limit = kwargs.get('limit', None)
        
        
==============================
    def rebuild(self, context, instance, image_href, admin_password,
                files_to_inject=None, **kwargs):
        """Rebuild the given instance with the provided attributes."""
        orig_image_ref = instance.image_ref or ''
        files_to_inject = files_to_inject or []
        metadata = kwargs.get('metadata', {})
        preserve_ephemeral = kwargs.get('preserve_ephemeral', False)
        auto_disk_config = kwargs.get('auto_disk_config')
        

kwargs = {'metadata': {},
          'preserve_ephemral'}
          
