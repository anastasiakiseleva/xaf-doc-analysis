---
uid: DevExpress.ExpressApp.Controller.Deactivated
name: Deactivated
type: Event
summary: Occurs after a [](xref:DevExpress.ExpressApp.Controller) has been deactivated.
syntax:
  content: public event EventHandler Deactivated
seealso:
- linkId: DevExpress.ExpressApp.Controller.Activated
---
[comment]: <> (<\!--<para>A Controller is deactivated when the <see cref="P:DevExpress.ExpressApp.Controller.Active"/> collection gets an element with the <i>value</i> part set to <b>false</b>.</para>)
[comment]: <> (<note>View Controllers are deactivated before setting <b>null</b> for their <see cref="P:DevExpress.ExpressApp.ViewController.View"/> property. Window Controllers are deactivated before setting <b>null</b> for their <see cref="P:DevExpress.ExpressApp.WindowController.Window"/> property. </note>-->)

The **Deactivated** event is raised if the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) collection gets an element with the _value_ part set to **false**.

> [!NOTE]
> A View Controller is deactivated before its [ViewController.View](xref:DevExpress.ExpressApp.ViewController.View) property is set to **null**. A Window Controller is deactivated before its [WindowController.Window](xref:DevExpress.ExpressApp.WindowController.Window) property is set to **null**.

For details on how to use Controllers, refer to the [Controllers](xref:112621) topic.