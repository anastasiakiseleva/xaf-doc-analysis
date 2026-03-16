---
uid: DevExpress.ExpressApp.Win.SystemModule.WinModificationsController
name: WinModificationsController
type: Class
summary: Inherits from the [](xref:DevExpress.ExpressApp.SystemModule.ModificationsController) to implement Windows Forms specific behavior.
syntax:
  content: 'public class WinModificationsController : ModificationsController'
seealso:
- linkId: DevExpress.ExpressApp.Win.SystemModule.WinModificationsController._members
  altText: WinModificationsController Members
---
The **WinModificationsController** adds the following functionality to the base [](xref:DevExpress.ExpressApp.SystemModule.ModificationsController):

* **Save** Action
    
    When executing the **Save** Action, the Controller commits the changes .
    
    The Action is deactivated in List Views if the [ModificationsController.ModificationsHandlingMode](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsHandlingMode) property is set to [ModificationsHandlingMode.AutoCommit](xref:DevExpress.ExpressApp.SystemModule.ModificationsHandlingMode.AutoCommit).
    
    The Action is disabled when the current object is not modified.
* **SaveAndClose** Action
    
    When executing the **SaveAndClose** Action, the Controller commits the changes made to the current object and closes the current View.
    
    The Action is deactivated in List Views if the [ModificationsController.ModificationsHandlingMode](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsHandlingMode) property is set to [ModificationsHandlingMode.AutoCommit](xref:DevExpress.ExpressApp.SystemModule.ModificationsHandlingMode.AutoCommit).
* **Cancel** Action
    
    Rolls back the changes made to the current object (see [BaseObjectSpace.Rollback](xref:DevExpress.ExpressApp.BaseObjectSpace.Rollback(System.Boolean))) and retrieves the object from the database again.
    
    The Action is deactivated in List Views if the [ModificationsController.ModificationsHandlingMode](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsHandlingMode) property is set to [ModificationsHandlingMode.AutoCommit](xref:DevExpress.ExpressApp.SystemModule.ModificationsHandlingMode.AutoCommit).
    
    The Action is set to disabled, when the data is not modified.
* **UpdateActionState** method
    
    Overrides this method to check whether to update the **Save**, **Cancel** and **SaveAndClose** Actions' enabled state, depending on whether the current object has been modified or the AutoCommitListView property value has changed. The **SaveAndNew** Action is activated for Detail Views only.