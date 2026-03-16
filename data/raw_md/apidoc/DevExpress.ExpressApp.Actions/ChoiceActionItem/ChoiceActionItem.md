---
uid: DevExpress.ExpressApp.Actions.ChoiceActionItem
name: ChoiceActionItem
type: Class
summary: An item of the [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) Action.
syntax:
  content: 'public class ChoiceActionItem : IComplexChoiceAction, ISupportClientScripts, ISecuredAction'
seealso:
- linkId: DevExpress.ExpressApp.Actions.ChoiceActionItem._members
  altText: ChoiceActionItem Members
---
The **XAF** supplies the [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) which can be used to execute custom code when an end-user selects one of its items. These items are represented by the **ChoiceActionItem** class and contained in the [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection. To add items to this collection, use the ellipsis button provided by the Single Choice Action's Items property in the **Properties** window. Via this button, you can invoke the**ChoiceActionItem Collection Editor**, which allows you to specify settings of the collection's items.

A Choice Action Item can contain nested Items, which can contain Items as well. So, an Item can serve as a parent for a collection of items. This collection is accessed via the [ChoiceActionItem.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.Items) property. To populate this collection at design time, use the **ChoiceActionItem Collection Editor**.

![ChoiceActionItem_Items](~/images/choiceactionitem_items115416.png)

In some scenarios, you can create Choice Action Items and add them to the [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection of the required Single Choice Action in the Controller's constructor code. In the Main Demo, you can see an example where the created Choice Action Items represent an enumeration's values (see [Add an Action with Option Selection](xref:402159)). In this instance, they cannot be created at design time.

The Choice Action Items that are added to a Single Choice Action at design time or in the Controller's constructor are loaded to the [Application Model](xref:112580). So, you can invoke the [Model Editor](xref:112830) and use the **ActionDesign**  | **Actions** | **Action** | **ChoiceActionItems** node to set images, shortcuts and localized captions for the Choice Action Items of the required Action. However, there can be scenarios when you have to create Choice Action Items in the Controller's [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event handler, because the Application, View and other objects are available when this event is raised. In this instance, the created items will not be loaded to the Application Model.

You can make a Choice Action Item enabled or disabled. For this purpose, use the [ChoiceActionItem.Enabled](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.Enabled) method. To indicate whether the Item is currently enabled, use the same method in a conditional expression.  Alternatively, use the [BoolList.ResultValue](xref:DevExpress.ExpressApp.Utils.BoolList.ResultValue) property of the object returned by the [ChoiceActionItem.Enabled](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.Enabled) property.

To associate a Choice Action Item with an object, use its [ChoiceActionItem.Data](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.Data) property.

If you need to implement a Choice Action that differs from the [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction), you can use this class to present the Action's Items.
