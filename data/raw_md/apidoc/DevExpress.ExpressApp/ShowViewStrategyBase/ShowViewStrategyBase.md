---
uid: DevExpress.ExpressApp.ShowViewStrategyBase
name: ShowViewStrategyBase
type: Class
summary: An abstract class that serves as the base class for the Show View Strategy classes.
syntax:
  content: 'public abstract class ShowViewStrategyBase : IDisposable'
seealso:
- linkId: DevExpress.ExpressApp.ShowViewStrategyBase._members
  altText: ShowViewStrategyBase Members
---
A Show View Strategy is an object that manages the display of [Views](xref:112611) in a UI. When an XAF application needs to display a View in a UI, it is the application's Show View Strategy that decides where and how to display the View. For example, if you don't specify the [](xref:DevExpress.ExpressApp.Frame) that should display the View, the Show View Strategy resolves the following questions:

* Should XAF display the View in an existing Frame?
* Should XAF create a new [](xref:DevExpress.ExpressApp.Window)?
* If XAF should create a new Window, must it be modal?

A Show View Strategy has two main tasks: decide where and how a View should appear, and display the View in the UI.

Consider the following example. When a user clicks a record in a List View that is displayed in the main Window, XAF must invoke a Detail View. This Detail View can be displayed in a UI in different ways. One of the available options is to display the Detail View in a new Window:

![SVStrategy1](~/images/svstrategy1116268.png)

![SVStrategy3](~/images/svstrategy3116270.png)

Another option is to display the Detail View in the same Window:

![SVStrategy1](~/images/svstrategy1116268.png)

![SVStrategy2](~/images/svstrategy2116269.png)

Additional options are available. For example, you can use a multiple document interface (MDI), so that a new View is displayed in a separate tab within the main Window.

A Show View Strategy has a set of rules that govern all possible scenarios defined within the Strategy. The example above illustrates only one kind of rule - how to display a Detail View invoked from a List View that is displayed in the main Window. Each Strategy, however, has many additional rules -- a set of rules for the nested Views, Views that are displayed by the [Lookup Property Editors](xref:113014), and so on.

An XAF application instantiates a Show View Strategy when the application starts. It assigns the specific Show View Strategy that the application must use to the [XafApplication.ShowViewStrategy](xref:DevExpress.ExpressApp.XafApplication.ShowViewStrategy) property.

The `ShowViewStrategyBase` class is an abstract class from which all Show View Strategies are derived. The following table lists XAF's built-in Show View Strategies:

| ShowViewStrategyBase Descendant | Description |
|---|---|
| `DevExpress.ExpressApp.Blazor.BlazorMdiShowViewStrategy` | Used in XAF ASP.NET Core Blazor applications. Displays a new View in a separate tab within the main Window. |
|`DevExpress.ExpressApp.Blazor.BlazorShowViewStrategy`| Used in XAF ASP.NET Core Blazor applications. Displays a new View in the main Window. |
| [](xref:DevExpress.ExpressApp.Win.WinShowViewStrategyBase) | An abstract class from which all Show View Strategies used in the XAF Windows Forms applications are derived. |
| [](xref:DevExpress.ExpressApp.Win.ShowInMultipleWindowsStrategy) | Used by default in XAF Windows Forms applications. |
| [](xref:DevExpress.ExpressApp.Win.ShowInSingleWindowStrategy) | A Show View Strategy that can be used as an alternative to the `ShowInMultipleWindowsStrategy`. A Detail View is invoked from a List View that is displayed in the main Window. |
| [](xref:DevExpress.ExpressApp.Win.MdiShowViewStrategy) | Another alternative to the `ShowInMultipleWindowsStrategy`. Uses multiple-document interface (MDI). |
