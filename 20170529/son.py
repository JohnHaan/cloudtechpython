def is_admin(username):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("aaaaaa")
        return func(*args, **kwargs)
    return wrapper


class Greet(object):
    cur_user = None
        
    @is_admin
    def set_name(self, username):
        self.cur_user = name

    @is_admin
    def get_greeting(self, username):
        print("Hello {}".format(self.cur_user))
            
            
greet = Greet()
greet.set_name('admin')
greet.get_greeting('son')