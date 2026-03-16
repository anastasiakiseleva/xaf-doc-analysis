---
uid: DevExpress.ExpressApp.Blazor.SystemModule.BlazorModificationsController
name: BlazorModificationsController
type: Class
summary: Inherits from the [](xref:DevExpress.ExpressApp.SystemModule.ModificationsController) to implement ASP.NET Core Blazor specific behavior.
syntax:
  content: 'public class BlazorModificationsController : ModificationsController'
seealso:
- linkId: DevExpress.ExpressApp.Blazor.SystemModule.BlazorModificationsController._members
  altText: BlazorModificationsController Members
---
The `BlazorModificationsController` adds the following functionality to the base [](xref:DevExpress.ExpressApp.SystemModule.ModificationsController):

* **Save** Action

    Commits the changes made to the current object. This Action is hidden from List Views.

* **Save and New** Action

    Commits the changes made to the current object and creates a new object.

* **Save and Close** Action
    
    Commits the changes made to the current object and closes the current View.

* **Cancel** Action
    
    This Action is inactive in ASP.NET Core Blazor applications.