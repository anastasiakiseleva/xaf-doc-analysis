---
uid: DevExpress.ExpressApp.Utils.BoolValueChangedEventArgs
name: BoolValueChangedEventArgs
type: Class
summary: Represents arguments passed to the [BoolList.ResultValueChanged](xref:DevExpress.ExpressApp.Utils.BoolList.ResultValueChanged) event.
syntax:
  content: 'public class BoolValueChangedEventArgs : EventArgs'
seealso:
- linkId: DevExpress.ExpressApp.Utils.BoolValueChangedEventArgs._members
  altText: BoolValueChangedEventArgs Members
---
The **BoolValueChangedEventArgs** class exposes two properties. The [BoolValueChangedEventArgs.OldValue](xref:DevExpress.ExpressApp.Utils.BoolValueChangedEventArgs.OldValue) property represents the old **ResultValue** of the **BoolList**. The [BoolValueChangedEventArgs.NewValue](xref:DevExpress.ExpressApp.Utils.BoolValueChangedEventArgs.NewValue) property represents the new **ResultValue** of the **BoolList**.

The **ResultValueChanged** event occurs after the resulting value of a [](xref:DevExpress.ExpressApp.Utils.BoolList) has changed. You can handle this event to be notified when the [BoolList.ResultValue](xref:DevExpress.ExpressApp.Utils.BoolList.ResultValue) is changed.