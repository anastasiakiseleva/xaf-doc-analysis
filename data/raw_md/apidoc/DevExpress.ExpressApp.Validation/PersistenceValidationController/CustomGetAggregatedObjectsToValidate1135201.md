---
uid: DevExpress.ExpressApp.Validation.PersistenceValidationController.CustomGetAggregatedObjectsToValidate
name: CustomGetAggregatedObjectsToValidate
type: Event
summary: Occurs when determining which aggregated objects should be validated.
syntax:
  content: public event EventHandler<CustomGetAggregatedObjectsToValidateEventArgs> CustomGetAggregatedObjectsToValidate
seealso: []
---
Handle this event to manually specify the **OwnerObject**'s aggregated objects to be validated. By default, all aggregated objects are validated. To create the list of objects to be validated manually, add these objects to the **AggregatedObjects** list and set the **Handled** parameter to **true**.

Validation may take significant time when an object to be saved exposes a large collection of aggregated objects. By default, aggregated objects are considered to be an integral part of a master object, and thus, they should be validated together with the master object. The entire collection will be loaded in this instance. However, you can use the **CustomGetAggregatedObjectsToValidate** event to change this behavior and cancel validating the aggregated objects that are not updated. You can use the [IObjectSpace.IsObjectToSave](xref:DevExpress.ExpressApp.IObjectSpace.IsObjectToSave(System.Object)) method to ensure that a certain object is not modified.

# [C#](#tab/tabid-csharp)

```csharp
void CustomGetAggregatedObjectsToValidate(object sender, CustomGetAggregatedObjectsToValidateEventArgs e) {
    if (e.OwnerObject is Contact) {
        foreach (PhoneNumber number in ((Contact)e.OwnerObject).PhoneNumbers) {
            if (ObjectSpace.IsObjectToSave(number)) {
                e.AggregatedObjects.Add(number);
            }
        }
    }
    e.Handled = true;
}
```
***

> [!IMPORTANT]
> The drawback of this approach is that invalid aggregated objects that were added before the rule is introduced, or created in the database directly, will be skipped.

See the another example of using the **CustomGetAggregatedObjectsToValidate** event in the [](xref:DevExpress.ExpressApp.Validation.PersistenceValidationController) class description.