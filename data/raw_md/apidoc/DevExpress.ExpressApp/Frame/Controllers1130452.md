---
uid: DevExpress.ExpressApp.Frame.Controllers
name: Controllers
type: Property
summary: Provides access to the [Controller](xref:112621) collection.
syntax:
  content: public LightDictionary<Type, Controller> Controllers { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Utils.LightDictionary{System.Type,DevExpress.ExpressApp.Controller}
    description: A **LightDictionary\<Type, Controller>** object representing a Controller collection.
seealso: []
---
Each [](xref:DevExpress.ExpressApp.Frame) (and [](xref:DevExpress.ExpressApp.Window), consequently) has a **Controller** collection. To access, add or remove a Controller from this collection, use members of the **LightDictionary\<Type, Controller>** object (Key, Value, Next, AddItem, FindItem, etc.), which is returned by the **Controllers** property. To access a particular Controller, use the **GetController\<ControllerType>** method.