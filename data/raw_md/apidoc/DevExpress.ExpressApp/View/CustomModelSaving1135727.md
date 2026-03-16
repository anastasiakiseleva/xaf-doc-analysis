---
uid: DevExpress.ExpressApp.View.CustomModelSaving
name: CustomModelSaving
type: Event
summary: Occurs when saving information on a View's editor(s) to the [Application Model](xref:112580).
syntax:
  content: |-
    [Browsable(false)]
    public event EventHandler<HandledEventArgs> CustomModelSaving
seealso:
- linkId: DevExpress.ExpressApp.View.ModelSaving
- linkId: DevExpress.ExpressApp.View.ModelSaved
---
This event is raised when calling the current View's [View.SaveModel](xref:DevExpress.ExpressApp.View.SaveModel) method. This method is used to save settings of the [View Items](xref:112612) and their layout for a Detail View and settings of the [List Editor](xref:113189) for a List View. These settings are saved to the Application Model node specified by the View's [View.Model](xref:DevExpress.ExpressApp.View.Model) property current value. Handle this event to implement a custom technique of saving information on a View. Set the handler's **HandledEventArgs.Handled** parameter to **true**, to cancel the default saving process.