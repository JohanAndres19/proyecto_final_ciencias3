from os import mkdir, name
from os.path import exists, dirname, join
import jinja2
from entity_test import get_entity_mm

def main(debug=False):

    this_folder = dirname(__file__)

    entity_mm = get_entity_mm(debug)
    
    calculator_model = entity_mm.model_from_file(join(this_folder,'calculadora.en'))

    def is_variable(n):
        if n in calculator_model.variable:
            return True
        else:
            return False

    def is_void(n):
        if n.name == 'void':
            return True
        else:
            return False 

    def is_main(n):
        if n.name == 'main':
            return True
        else:
            return False       
    
    def javatype(s):
        """
        Maps type names from SimpleType to Java.
        """
        return {
                'INT': 'int',
                'void': 'void'
        }.get(s.name, s.name)

    def is_constructor(n):
        if n.name =='constructor':
            return True
        else:
            return False  
    
    def tamaño(n):
        return len(n)

    def is_suma(n):
        if n.name == 'sumar':
            return True
        else:
            return False

    def is_resta(n):
        if n.name == 'restar':
            return True
        else:
            return False
    
    def is_multi(n):
        if n.name == 'multiplicar':
            return True
        else:
            return False

    def is_division(n):
        if n.name == 'division':
            return True
        else:
            return False

    # Create output folder
    srcgen_folder = join(this_folder, 'srcgen')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    
    # Register filter for mapping Entity type names to Java type names.

    #jinja_env.tests['entity'] = is_entity
    
    #jinja_env.filters['javatype'] = javatype
    jinja_env.filters['javatype'] = javatype
    jinja_env.filters['tamaño']= tamaño
    jinja_env.tests['variable'] = is_variable
    jinja_env.tests['main'] = is_main
    jinja_env.tests['void'] = is_void
    jinja_env.tests['constructor']=is_constructor
    jinja_env.tests['suma']=is_suma
    jinja_env.tests['resta']=is_resta
    jinja_env.tests['multi']=is_multi
    jinja_env.tests['division']=is_division
    template = jinja_env.get_template('class.template')

    
        # For each entity generate java file
    with open(join(srcgen_folder,
                       "%s.java" % calculator_model.name.capitalize()), 'w') as f:
            f.write(template.render(entity=calculator_model))

    
            
if __name__ == "__main__":
    main()