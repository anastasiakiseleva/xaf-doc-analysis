---
uid: DevExpress.ExpressApp.Win.WinShowViewStrategyBase
name: WinShowViewStrategyBase
type: Class
summary: An abstract class that serves as the base class for Show View Strategies used in **XAF** Windows Forms applications.
syntax:
  content: 'public abstract class WinShowViewStrategyBase : ShowViewStrategyBase'
seealso:
- linkId: DevExpress.ExpressApp.Win.WinShowViewStrategyBase._members
  altText: WinShowViewStrategyBase Members
---
The following table lists the built-in Show View Strategies that derive from the **WinShowViewStrategyBase**.

| **WinShowViewStrategyBase Descendant** | Description |
|---|---|
| [](xref:DevExpress.ExpressApp.Win.ShowInMultipleWindowsStrategy) | Used by default in **XAF** Windows Forms applications. |
| [](xref:DevExpress.ExpressApp.Win.ShowInSingleWindowStrategy) | A Show View Strategy that can be used as an alternative to the **ShowInMultipleWindowsStrategy**. Provides different behavior when a Detail View is invoked from a List View that is displayed in the main Window. |
| [](xref:DevExpress.ExpressApp.Win.MdiShowViewStrategy) | Another alternative to the **ShowInMultipleWindowsStrategy**. Uses multiple document interface. |

[comment]: <> (<\!--)
[comment]: <> (<para>)
[comment]: <> (While implementing a custom Show View Strategy that inherits from the <b><%ClassName%></b>, the following protected methods, in addition to the methods described in the <see cref="T:DevExpress.ExpressApp.ShowViewStrategyBase"/> class description, not described in the documentation, can be overridden.)
[comment]: <> (</para>)
[comment]: <> (<list type="table">)
[comment]: <> (<listheader>)
[comment]: <> (<term>Member Name</term><description>Description</description>)
[comment]: <> (</listheader>)
[comment]: <> (<item><term><b>AfterAddWindow</b></term><description>Called after a window is added to the <see cref="P:DevExpress.ExpressApp.Win.WinShowViewStrategyBase.Explorers"/> collection. Specifies the code that must be performed before a created window is shown.</description></item>)
[comment]: <> (<item><term><b>ShowInModalWindow</b></term><description>Displays a View passed to a <see cref="M:DevExpress.ExpressApp.ShowViewStrategyBase.ShowView"/> method in a new modal Window.</description></item>)
[comment]: <> (<item><term><b>ShowViewInNewWindow</b></term><description>Displays a View passed to a <see cref="M:DevExpress.ExpressApp.ShowViewStrategyBase.ShowView"/> method in a Window from which the <b>ShowView</b> method was invoked.</description></item>)
[comment]: <> (</list>)
[comment]: <> (-->)

By default, **XAF** Windows Forms applications use the [](xref:DevExpress.ExpressApp.Win.ShowInMultipleWindowsStrategy). To use another Strategy, specify the [Application Model](xref:112580)'s [IModelOptionsWin.UIType](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.UIType) property of the Application | Options node. Alternatively, you can manually instantiate the required Strategy and assign it to the [XafApplication.ShowViewStrategy](xref:DevExpress.ExpressApp.XafApplication.ShowViewStrategy) property.

For general information on Show View Strategies, refer to the [](xref:DevExpress.ExpressApp.ShowViewStrategyBase) class description.