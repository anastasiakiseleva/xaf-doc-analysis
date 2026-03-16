---
uid: DevExpress.ExpressApp.Win.ShowInSingleWindowStrategy
name: ShowInSingleWindowStrategy
type: Class
summary: A Show View Strategy that can be used as an alternative to the [](xref:DevExpress.ExpressApp.Win.ShowInMultipleWindowsStrategy). Provides a different behavior when a Detail View is invoked from a List View that is displayed in the main Window.
syntax:
  content: 'public class ShowInSingleWindowStrategy : WinShowViewStrategyBase'
seealso:
- linkId: DevExpress.ExpressApp.Win.ShowInSingleWindowStrategy._members
  altText: ShowInSingleWindowStrategy Members
---
According to this Strategy, when a Detail View is invoked from a root (see [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot)) List View that is displayed in the main Window, the Detail View must replace the List View in the main Window:

![SVStrategy1](~/images/svstrategy1116268.png)

![SVStrategy2](~/images/svstrategy2116269.png)

By default, **XAF** Windows Forms applications use the [](xref:DevExpress.ExpressApp.Win.ShowInMultipleWindowsStrategy). To use another Strategy, specify the [Application Model](xref:112580)'s [IModelOptionsWin.UIType](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.UIType) property of the Application | Options node. Alternatively, you can manually instantiate the required Strategy and assign it to the [XafApplication.ShowViewStrategy](xref:DevExpress.ExpressApp.XafApplication.ShowViewStrategy) property.

For general information on Show View Strategies, refer to the [](xref:DevExpress.ExpressApp.ShowViewStrategyBase) class description.