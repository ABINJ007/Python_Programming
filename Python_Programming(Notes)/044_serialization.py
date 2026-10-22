'''
Serialization:
    -process of converting an object (data structure) into a format, that can be
     stored or transmitted
    -The format is usually:
        text(JSON)
        binary(pickle)

    -NON TEXT python objects such as int, float , list, dict, None needs conversion
     before storage into a file and that's whey we use json module.

JSON Module:
------------
    -it converts "structured data" ->text
    -Text can be safely written to files.
    -Structure can be reliably restored.

1)Dumps()
---------
    Syntax:
        json_str=json.dumps(obj)

    -dumps() is a function of json module that converts a python object into a JSON
     formatted string.

2)Dump()
    Syntax:
        json.dump(obj, f)

    -dump() is jsonn module function that converts a python object into JSON format
     and writes it into a file.


Deserialisation:
---------------
    -process of converting stored/transmitted data back to an object(data structure)

1)loads()
    Syntax:
        Python_obj=json.loads(json_string)

    -loads function of json module reconvert a JSON string back to the python object

2)load()
    Syntax:
        Python_obj=json.load(f)

    -loads() function of json module reads JSON data from a file and convert it
     into a python object.

Pickle Module:
--------------
    -Pickling Converts a python object into a byte stream(binary data) and stores
     it in a binary file.

1)dumps()
    Syntax:
        byte_data=Pickle.dumps(obj)

    -dumps() is function of the pickle module that converts a python object into a
     byte stream.

2)dump()
    Syntax:
        pickle.dump(obj,f)
    -dump() is a function of the pickle module that converts a python object into a
     byte stream and writes it into a binary file.

Unpickling:
-----------
    -is the process of converting a byte stream(binarydata) back into the original
     python object.

1)loads()
    Syntax:
        obj=pickle.loads(byte_data)

    -loads() is a function of the pickle module that converts a byte stream back into a python object.

2)load()
    Syntax:
        obj=pickle.load(f)
    -load() is a function of the pickle module that reads a byte stream from a binary file and converts
     it back into a python object.
'''
     
     
