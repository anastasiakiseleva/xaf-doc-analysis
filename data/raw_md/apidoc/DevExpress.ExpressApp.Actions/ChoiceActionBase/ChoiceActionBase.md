---
uid: DevExpress.ExpressApp.Actions.ChoiceActionBase
name: ChoiceActionBase
type: Class
summary: Represents the ancestor for [Actions](xref:112622) that provide items to be chosen by an end-user.
syntax:
  content: 'public abstract class ChoiceActionBase : ActionBase, IComplexChoiceAction'
seealso:
- linkId: DevExpress.ExpressApp.Actions.ChoiceActionBase._members
  altText: ChoiceActionBase Members
---
Currently, the **ChoiceActionBase** class has a single descendant - the [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction). This descendant allows end-users to select a single item in the [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection. This collection is provided by the ChoiceActionBase class.  Each collection item can have child items as well. So, you can form a tree within this collection.

You can specify how to display a Choice Action, if its Items collection is empty. For instance, this Action can be disabled or made invisible (see [ChoiceActionBase.EmptyItemsBehavior](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.EmptyItemsBehavior)).

You can specify whether to execute a Choice Action when clicking it, or show its drop-down with items (see [ChoiceActionBase.ShowItemsOnClick](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.ShowItemsOnClick)). To specify the Choice Action Item that is executed by default, use the [ChoiceActionBase.DefaultItemMode](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.DefaultItemMode) property. You can set whether to always execute the first active item in Items collection or to execute the previously executed item.