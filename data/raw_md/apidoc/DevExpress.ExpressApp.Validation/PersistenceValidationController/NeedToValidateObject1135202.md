---
uid: DevExpress.ExpressApp.Validation.PersistenceValidationController.NeedToValidateObject
name: NeedToValidateObject
type: Event
summary: Occurs when determining objects to be validated.
syntax:
  content: public event EventHandler<NeedToValidateObjectEventArgs> NeedToValidateObject
seealso: []
---
Handle this event to exclude particular objects from validation. This event is triggered for each object that is about to be validated. To exclude particular objects from validation, check that the object specified by the **CurrentObject** property fits your criteria and set the **NeedToValidate** property to **false**.