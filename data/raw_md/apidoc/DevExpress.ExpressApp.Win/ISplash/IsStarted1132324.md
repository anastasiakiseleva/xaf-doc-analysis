---
uid: DevExpress.ExpressApp.Win.ISplash.IsStarted
name: IsStarted
type: Property
summary: Indicates whether the splash screen is being displayed.
syntax:
  content: bool IsStarted { get; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the splash screen is being displayed; otherwise, **false**.'
seealso: []
---
When implementing a custom splash screen, generally you need to do the following:

* Initialize this property to **false**.
* In the [ISplash.Start](xref:DevExpress.ExpressApp.Win.ISplash.Start) method, set this property to **true**.
* In the [ISplash.Stop](xref:DevExpress.ExpressApp.Win.ISplash.Stop) method, set this property to **false**.