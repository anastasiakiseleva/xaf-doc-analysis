---
uid: DevExpress.ExpressApp.SystemModule.ProcessDataLockingInfoController
name: ProcessDataLockingInfoController
type: Class
summary: Use this controller to implement custom strategies of conflict detection and resolution.
syntax:
  content: 'public class ProcessDataLockingInfoController : ObjectViewController'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.ProcessDataLockingInfoController._members
  altText: ProcessDataLockingInfoController Members
---

When you execute **Save**, **Save and New**, or **Save and Close** Actions, this controller calls the Object Space code that collects the following information:

* Local modified objects 
* Objects modified by other users 
* Conflict detection and resolution strategies implemented in your application

You can access and modify this information in the @DevExpress.ExpressApp.SystemModule.ProcessDataLockingInfoController.DataLockingProcessing event.

[!include[](~/templates/optimisticlock-automerge.md)]