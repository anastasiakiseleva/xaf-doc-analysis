---
uid: DevExpress.ExpressApp.Utils.BoolList.Contains(System.String)
name: Contains(String)
type: Method
summary: Indicates whether a particular key exists in the [](xref:DevExpress.ExpressApp.Utils.BoolList)'s collection of key/value pairs.
syntax:
  content: public bool Contains(string key)
  parameters:
  - id: key
    type: System.String
    description: A string representing the key that will be checked for existence in the **BoolList**'s collection of key/value pairs.
  return:
    type: System.Boolean
    description: "**true**, if the specified key exists in the **BoolList**'s collection of key/value pairs; otherwise, **false**."
seealso: []
---
You can use this method, prior to reading the value associated with a key, via the [BoolList.Item](xref:DevExpress.ExpressApp.Utils.BoolList.Item(System.String)) indexer property, to check that a key/value pair exists for the key. The following code snippet illustrates this.

# [C#](#tab/tabid-csharp)

```csharp
BoolList mylist = new BoolList();
//...
Boolean myValue = false;
if (mylist.Contains("myKey")) {
    myValue = mylist["myKey"];
}
```
***

To get all keys from the **BoolList**'s collection of key/value pairs, use the [BoolList.GetKeys](xref:DevExpress.ExpressApp.Utils.BoolList.GetKeys) method.