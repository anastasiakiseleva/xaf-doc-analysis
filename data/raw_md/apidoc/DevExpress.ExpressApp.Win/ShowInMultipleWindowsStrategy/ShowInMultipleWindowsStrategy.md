---
uid: DevExpress.ExpressApp.Win.ShowInMultipleWindowsStrategy
name: ShowInMultipleWindowsStrategy
type: Class
summary: Represents the Show View Strategy used in **XAF** Windows Forms applications by default.
syntax:
  content: 'public class ShowInMultipleWindowsStrategy : WinShowViewStrategyBase'
seealso:
- linkId: DevExpress.ExpressApp.Win.ShowInMultipleWindowsStrategy._members
  altText: ShowInMultipleWindowsStrategy Members
---
According to this strategy, each [View](xref:112611) should be displayed in a new [](xref:DevExpress.ExpressApp.Window), whenever possible.

![ShowInMultipleWindowsStrategy](~/images/showinmultiplewindowsstrategy116267.png)

Since this strategy is used by default in **XAF** Windows Forms applications, there is generally no need to instantiate it in your code.

**XAF** is shipped with another built-in Show View Strategies that can be used, instead of the **ShowInMultipleWindowsStrategy** - the [](xref:DevExpress.ExpressApp.Win.ShowInSingleWindowStrategy) and [](xref:DevExpress.ExpressApp.Win.MdiShowViewStrategy).

For general information on Show View Strategies, refer to the [](xref:DevExpress.ExpressApp.ShowViewStrategyBase) class description.