import admin_shortened_module as asm
import user_module as um
import priviledges_module as pm

admin_new = asm.Admin('alice', 'smith', location='Canada', age='30',
                      years_of_experience='8')

admin_new.list_of_admin_priviledges.show_priviledges()

