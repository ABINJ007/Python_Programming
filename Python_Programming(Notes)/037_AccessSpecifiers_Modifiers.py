'''
AccessSpecifiers/Modifiers:
    ->It applies only inside classes, a because classes are about encapsulation
    ->these are used to specify the visibility or accessibility of variables or
    methods
3Types
1)Public
    2)Protected
    3)Private

    1)Public:
    -> any var or method declared normally inside a class is by default considered
    as public
    -> No leading underscore are used for it
    -> such var or methods can be accessed from anywhere(from inside class or from
                                                         outside class in samemodule or outside module in samepackage)

    2)protected:
    -> any var or method declared using "single leading underscore" inside a class
    considered as protected
    -> protected is meant for internal usage by child class
    -> it shud be used either in same class or its child classes and This is
    CONVENTION not an enforcement

    3)Private:
    -> Any var or method declared using "double leading underscore" inside a class
    considered as private

    -> Private cannot be accessed directly from outside the class , it be accessed
    only from inside the class using methods

    -> used specially to hide sensitive data
'''