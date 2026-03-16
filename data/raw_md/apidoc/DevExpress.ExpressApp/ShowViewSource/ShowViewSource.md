---
uid: DevExpress.ExpressApp.ShowViewSource
name: ShowViewSource
type: Class
summary: Contains a set of parameters that specify the current view context.
syntax:
  content: public class ShowViewSource
seealso:
- linkId: DevExpress.ExpressApp.ShowViewSource._members
  altText: ShowViewSource Members
---
When an XAF application needs to display a [View](xref:112611), the application calls the `ShowView` method. To correctly display the View, the `ShowView` method requires information on the current context in the form of a `ShowViewSource` object. For this purpose, the `ShowViewSource` class exposes the following public properties.

|  |  |
|---|---|
| `SourceAction` | If a View has to be displayed as the result of an [Action](xref:112622), this property contains reference to the Action's instance. |
| `SourceController` | If a View has to be displayed as the result of an `Action`, this property contains reference to the instance of the [Action](xref:112622)'s [](xref:DevExpress.ExpressApp.Controller). |
| `SourceView` | Contains a reference to the View that is represented by the Frame from which the `ShowView` method is invoked. |
| `SourceFrame` | Contains a reference to the Frame from which the `ShowView` method is invoked. |
