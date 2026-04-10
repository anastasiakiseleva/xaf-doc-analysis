Used for Type properties by default.
	
When you declare a Type property displayed with the help of **TypePropertyEditor**, apply the `System.ComponentModel.TypeConverter` attribute to it. In the attribute, pass the type of the converter that returns a collection of values representing data types in the Property Editor. For example, pass a built-in `LocalizedClassInfoTypeConverter`. It returns values of the `Caption` property of the corresponding **BOModel** | **_\<Class\>_** nodes.
	
If you do not use the `TypeConverter` attribute for a type property, XAF loads a string representation of found types to the editor's Items collection.