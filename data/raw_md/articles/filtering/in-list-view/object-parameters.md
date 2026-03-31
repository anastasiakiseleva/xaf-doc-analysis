---
uid: "113278"
seealso: []
title: Object Parameters
---
# Object Parameters

Object parameters are supported for legacy compatibility. XPO natively supports serialization/deserialization of persistent objects to/from strings. When serializing a persistent object, all conversions are performed automatically. When deserializing an object, you need to provide a session, which will be used to restore the object. For this purpose, use the **Session.ParseCriteria** method instead of **CriteriaOperator.Parse**. If you already have code that uses the regular **CriteriaOperator.Parse** method, you can wrap the method call with **Session.CreateParseCriteriaSessionScope**.

# [C#](#tab/tabid-csharp)

```csharp
using(mySession.CreateParseCriteriaSessionScope()) {
    //...
    CriteriaOperator.Parse("...");
    //...
}
```
***

In this instance, the existing **CriteriaOperator.Parse** method will correctly restore persistent objects in the "mySession" session.
