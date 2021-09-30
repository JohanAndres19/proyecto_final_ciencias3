from os import mkdir
from os.path import exists, dirname, join
import jinja2
from entity_test import get_entity_mm

def main(debug=False):

    this_folder = dirname(__file__)

    entity_mm = get_entity_mm(debug)
    # Build Person model from person.ent file
    calculator_model = entity_mm.model_from_file(join(this_folder,'calculadora.en'))
    """
    def is_entity(n):
        
        Test to prove if some type is an entity
    
        if n.type in calculator_model.entities:
            return True
        else:
            return False
    """
    def is_command(n):
        return True
        
    def javatype(s):
        """
        Maps type names from PrimitiveType to Java.
        """
        return {
                'void': 'void',
        }.get(s.name, s.name)

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
    
    jinja_env.filters['javatype'] = javatype

    jinja_env.tests['comandos'] = is_command    # Load template
    template = jinja_env.get_template('class.template')

    
        # For each entity generate java file
    with open(join(srcgen_folder,
                       "%s.java" % calculator_model.name.capitalize()), 'w') as f:
            f.write(template.render(entity=calculator_model))

    
            
if __name__ == "__main__":
    main()