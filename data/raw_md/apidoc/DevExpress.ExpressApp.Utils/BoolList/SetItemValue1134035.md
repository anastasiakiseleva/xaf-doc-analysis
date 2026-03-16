---
uid: DevExpress.ExpressApp.Utils.BoolList.SetItemValue(System.String,System.Boolean)
name: SetItemValue(String, Boolean)
type: Method
summary: Assigns a new value to a particular key from the [](xref:DevExpress.ExpressApp.Utils.BoolList)'s collection of key/value pairs.
syntax:
  content: public void SetItemValue(string key, bool value)
  parameters:
  - id: key
    type: System.String
    description: A string representing the key from the **BoolList**'s collection of key/value pairs, to which a new value will be assigned.
  - id: value
    type: System.Boolean
    description: A Boolean value to be assigned to the specified key.
seealso: []
---
If a key/value pair with the specified key does not exist, it is created.

The following code snippet illustrates use of the **SetItemValue** method:

# [C#](#tab/tabid-csharp)

```csharp
BoolList mylist = new BoolList();
mylist.SetItemValue("myKey", true); 
//myValue == true;
```
***

To get all keys from the **BoolList**'s collection of key/value pairs, use the [BoolList.GetKeys](xref:DevExpress.ExpressApp.Utils.BoolList.GetKeys) method. To check whether a particular key exists, use the [BoolList.Contains](xref:DevExpress.ExpressApp.Utils.BoolList.Contains(System.String)) method.