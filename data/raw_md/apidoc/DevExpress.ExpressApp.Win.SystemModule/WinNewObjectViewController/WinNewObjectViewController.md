---
uid: DevExpress.ExpressApp.Win.SystemModule.WinNewObjectViewController
name: WinNewObjectViewController
type: Class
summary: Inherits from the [](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController) to implement Windows Forms specific behavior.
syntax:
  content: 'public class WinNewObjectViewController : NewObjectViewController'
seealso:
- linkId: DevExpress.ExpressApp.Win.SystemModule.WinNewObjectViewController._members
  altText: WinNewObjectViewController Members
---
This Controller populates the [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection of the inherited **New** Action (see [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction)). To populate this collection, the [NewObjectViewController.CollectDescendantTypes](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.CollectDescendantTypes) and [NewObjectViewController.CollectCreatableItemTypes](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.CollectCreatableItemTypes) methods are used. The items added using the former method are delimited by a line from the items added using the latter method. So, there are two item groups. The first one contains the current [View](xref:112611)'s object type (see [ObjectView.ObjectTypeInfo](xref:DevExpress.ExpressApp.ObjectView.ObjectTypeInfo)) and its descendants. The second one contains the types that are listed in the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.SystemModule.IModelCreatableItems) node. This node is generated automatically. The business classes that use the [](xref:DevExpress.Persistent.Base.CreatableItemAttribute) or [](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) are added to it. In addition, you can add a class to this node via the [Model Editor](xref:112582).