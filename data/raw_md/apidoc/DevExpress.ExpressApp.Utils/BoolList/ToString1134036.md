---
uid: DevExpress.ExpressApp.Utils.BoolList.ToString
name: ToString()
type: Method
summary: Returns a string representation of the [](xref:DevExpress.ExpressApp.Utils.BoolList).
syntax:
  content: public override string ToString()
  return:
    type: System.String
    description: A string representing the **BoolList**.
seealso: []
---
The **ToString** method returns a string representation of the **BoolList**'s [BoolList.ResultValue](xref:DevExpress.ExpressApp.Utils.BoolList.ResultValue). If the **ResultValue** is **false**, it is postfixed by a list of the key/value pairs contained in the **BoolList**'s collection whose values are **false**.