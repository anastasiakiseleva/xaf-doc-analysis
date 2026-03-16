---
uid: DevExpress.ExpressApp.Validation.PersistenceValidationController.ContextValidating
name: ContextValidating
type: Event
summary: Occurs when validation rules associated with the **Delete** or **Save** validation contexts are about to be checked.
syntax:
  content: public event EventHandler<ContextValidatingEventArgs> ContextValidating
seealso: []
---
Handle this event to modify the collection of objects which will be validated in the current context. Check the current validation context using the **Context** property and add the required objects to the **TargetObjects** list.

See the example of using the **ContextValidating** event in the [](xref:DevExpress.ExpressApp.Validation.PersistenceValidationController) class description.