---
uid: DevExpress.ExpressApp.Utils.Guard.ArgumentNotNullOrEmpty(System.String,System.String)
name: ArgumentNotNullOrEmpty(String, String)
type: Method
summary: Ensures that a specific string argument is not a null reference, and is not an empty string.
syntax:
  content: public static void ArgumentNotNullOrEmpty(string argumentValue, string argumentName)
  parameters:
  - id: argumentValue
    type: System.String
    description: A string holding the value of the argument to check.
  - id: argumentName
    type: System.String
    description: A string holding the name of the argument to check.
seealso: []
---
If the specified string is a null reference of an empty string, an exception is thrown.