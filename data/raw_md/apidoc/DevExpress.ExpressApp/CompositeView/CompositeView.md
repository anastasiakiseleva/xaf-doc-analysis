---
uid: DevExpress.ExpressApp.CompositeView
name: CompositeView
type: Class
summary: A base class for [Views](xref:112611) that support [View Items layout](xref:112817).
syntax:
  content: 'public abstract class CompositeView : View'
seealso:
- linkId: DevExpress.ExpressApp.CompositeView._members
  altText: CompositeView Members
- linkId: "112611"
---
The `CompositeView` class is a base class for [Views](xref:112611) that support [View Items](xref:112612) layout. View Items are abstract entities displayed in a UI by various controls.

**View Items Collection**

The [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items) property exposes a collection of the Composite's View's View Items.

**Layout Customization**

View Items layout functionality enables automatic generation of Detail Views and offers multiple ways to customize the layout:

- **Design time** - Use the [Model Editor](xref:112582).
- **Runtime** - Use the Customization form.
- **Code** - Customize programmatically.

For detailed information about layout customization techniques, refer to the following topic: [View Items Layout Customization](xref:112817).

> [!NOTE]
> XAF has two Composite View types that fully support View Items layout:
> 
> - [Dashboard View](xref:DevExpress.ExpressApp.DashboardView)
> - [Detail View](xref:DevExpress.ExpressApp.DetailView).
> 
> The [List View](xref:DevExpress.ExpressApp.ListView) class also derives from `CompositeView`, but it does not support View Items layout.