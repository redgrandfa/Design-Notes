'''
copy existing objects without dependent on their concrete classes.
'''
# object’s fields may be private and not visible from outside
# Sometimes you only know the interface, but not its concrete class

'''Basic implementation
client code:
    {IPrototye exisiting}
    copy = exisiting.clone()

    interface IPrototye
        clone(): Prototype 
實現 class ConcretePrototye1
        # 利用建構式多載，傳自己去拷貝
        ConcretePrototye(prototype) {  (copy all fields) }
        clone(): Prototype { return new ConcretePrototye(this) }
實現 class ConcretePrototye2...
'''


'''Prototype registry implementation
provides an easy way to access frequently-used prototypes. It stores a set of pre-built objects that are ready to be copied

simplest prototype registry is a name → prototype hash map


    class Prototye PrototypeRegistry
        items : Prototype[] #聚合 
        addItem(key, value:Prototype) ...
        getBy___(key) ...   #搜索符合的

    interface IPrototye
        clone(): Prototype 
實現 class ConcretePrototye
    同上

    
You can implement the registry as a new factory class or put it in the base prototype class with a static method
'''

# =====
import copy


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:
    """
    Python provides its own interface of Prototype via 
    `copy.copy` 
    and
    `copy.deepcopy` functions. 
    And any class that wants to implement custom
    implementations have to override `__copy__` and `__deepcopy__` member
    functions.
    """

    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        """
        be called whenever someone calls
        `copy.copy` with this object
        """

        # First, create copies of the nested objects.
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        # clone the object itself, using the prepared clones of the nested objects.
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__.update(self.__dict__) #??

        return new

    def __deepcopy__(self, memo=None):
        """
        be called whenever someone calls
        `copy.deepcopy` with this object 

        What is the use of the argument `memo`? 
        Memo is the dictionary that is used by the `deepcopy` library 
        to prevent infinite recursive copies in instances of circular references. 
        Pass it to all the `deepcopy` calls you make in the `__deepcopy__` implementation 
        to prevent infinite recursions.
        """
        if memo is None:
            memo = {}

        # First, let's create copies of the nested objects.
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        # Then, let's clone the object itself, using the prepared clones of the
        # nested objects.
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new



list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
circular_ref = SelfReferencingEntity()
component = SomeComponent(23, list_of_objects, circular_ref)
circular_ref.set_parent(component)

shallow_copied_component = copy.copy(component)

# Let's change the list in shallow_copied_component and see if it changes in
# component.
shallow_copied_component.some_list_of_objects.append("another object") # 改到的是不同個
if component.some_list_of_objects[-1] == "another object":
    print(
        "Adding elements to `shallow_copied_component`'s "
        "some_list_of_objects adds it to `component`'s "
        "some_list_of_objects."
    )
else:  # 改到的是不同個，憶及 shallow_copied_component 和 component 不共用 some_list_of_objects
    print(
        "Adding elements to `shallow_copied_component`'s "
        "some_list_of_objects doesn't add it to `component`'s "
        "some_list_of_objects."
    )

component.some_list_of_objects[1].add(4) # 改到的是同一個
if 4 in shallow_copied_component.some_list_of_objects[1]:
    print( # 改到的是同一個，所以copy.copy預設只複製第一層(除非覆寫)，導致 element可能以address複製
        "Changing objects in the `component`'s some_list_of_objects "
        "changes that object in `shallow_copied_component`'s "
        "some_list_of_objects."
    )
else:
    print(
        "Changing objects in the `component`'s some_list_of_objects "
        "doesn't change that object in `shallow_copied_component`'s "
        "some_list_of_objects."
    )


#  ====================
deep_copied_component = copy.deepcopy(component)

deep_copied_component.some_list_of_objects.append("one more object") # 改到的是不同個
if component.some_list_of_objects[-1] == "one more object":
    print(
        "Adding elements to `deep_copied_component`'s "
        "some_list_of_objects adds it to `component`'s "
        "some_list_of_objects."
    )
else: # 改到的是不同個
    print(
        "Adding elements to `deep_copied_component`'s "
        "some_list_of_objects doesn't add it to `component`'s "
        "some_list_of_objects."
    )
component.some_list_of_objects[1].add(10) # 改到的是不同個
if 10 in deep_copied_component.some_list_of_objects[1]:
    print(
        "Changing objects in the `component`'s some_list_of_objects "
        "changes that object in `deep_copied_component`'s "
        "some_list_of_objects."
    )
else:  # 改到的是不同個
    print(
        "Changing objects in the `component`'s some_list_of_objects "
        "doesn't change that object in `deep_copied_component`'s "
        "some_list_of_objects."
    )

print(
    f"id(deep_copied_component.some_circular_ref.parent): "
    f"{id(deep_copied_component.some_circular_ref.parent)}"
)
print(
    f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): "
    f"{id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}"
)
# 兩者輸出的id相同  表示沒有循環拷貝，指拷貝到足夠層
print(
    "^^ This shows that deepcopied objects contain same reference, they "
    "are not cloned repeatedly."
)
