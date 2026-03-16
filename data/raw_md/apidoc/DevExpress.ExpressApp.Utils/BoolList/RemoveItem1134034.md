---
uid: DevExpress.ExpressApp.Utils.BoolList.RemoveItem(System.String)
name: RemoveItem(String)
type: Method
summary: Removes a key/value pair with a particular key from the [](xref:DevExpress.ExpressApp.Utils.BoolList)'s collection.
syntax:
  content: public void RemoveItem(string key)
  parameters:
  - id: key
    type: System.String
    description: A string representing the key of the key/value pair that will be removed from the **BoolList**'s collection.
seealso: []
---
The following code snippet illustrates use of the **RemoveItem** method:

# [C#](#tab/tabid-csharp)

```csharp
BoolList mylist = new BoolList();
mylist["myKey"] = true;
mylist.RemoveItem("myKey");
//mylist.Contains("myKey") == false;
```
***

To get all keys from the **BoolList**'s collection of key/value pairs, use the [BoolList.GetKeys](xref:DevExpress.ExpressApp.Utils.BoolList.GetKeys) method. To check whether a particular key exists, use the [BoolList.Contains](xref:DevExpress.ExpressApp.Utils.BoolList.Contains(System.String)) method.