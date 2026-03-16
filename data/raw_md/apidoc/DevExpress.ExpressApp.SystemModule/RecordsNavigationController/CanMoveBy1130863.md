---
uid: DevExpress.ExpressApp.SystemModule.RecordsNavigationController.CanMoveBy
name: CanMoveBy()
type: Method
summary: Indicates whether you can currently navigate to the previous object and\or next object.
syntax:
  content: public virtual RecordsNavigationController.MovementDirection CanMoveBy()
  return:
    type: DevExpress.ExpressApp.SystemModule.RecordsNavigationController.MovementDirection
    description: A **MovementDirection** enumeration value.
seealso: []
---
The following values are available:

* **MovementDirection.None**
    
    Navigation is not available to either the previous or next object.
* **MovementDirection.Forward**
    
    Navigation is available to the next object.
* **MovementDirection.Previous**
    
    Navigation is available to the previous object.
* **MovementDirection.All**
    
    Navigation is available to both the previous and next object.

This method is called by the **UpdateActionState** method, to determine whether to make the **NextObject** and **PreviousObject** Actions enabled\disabled.