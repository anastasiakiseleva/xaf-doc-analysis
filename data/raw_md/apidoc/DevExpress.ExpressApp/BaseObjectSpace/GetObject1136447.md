---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetObject(System.Object)
name: GetObject(Object)
type: Method
summary: Retrieves an object that corresponds to an @DevExpress.ExpressApp.IObjectRecord wrapper or object from another Object Space.
syntax:
  content: public virtual object GetObject(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An business object wrapper or object from another Object Space that corresponds to the required persistent object.
  return:
    type: System.Object
    description: An object retrieved from the database via the current Object Space.
seealso: []
---
This method does nothing and returns `null`. Override it in the `BaseObjectSpace` class' descendants.