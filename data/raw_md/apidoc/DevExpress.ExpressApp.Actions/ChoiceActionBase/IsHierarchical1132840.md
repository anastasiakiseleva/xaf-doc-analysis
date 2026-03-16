---
uid: DevExpress.ExpressApp.Actions.ChoiceActionBase.IsHierarchical
name: IsHierarchical()
type: Method
summary: Checks whether the Action's [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection has a tree-like structure.
syntax:
  content: public bool IsHierarchical()
  return:
    type: System.Boolean
    description: '**true** if there are Items containing other Items; otherwise **false**.'
seealso: []
---
The **IsHierarchical** method iterates through the Action's [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection (represented by the [](xref:DevExpress.ExpressApp.Actions.ChoiceActionItemCollection) class) and detects if there are child Items.

* **This method returns true**
    
    The items are displayed via a menu editor (in the tree mode).
    
    ![SingleChoiceAction_Tree](~/images/singlechoiceaction_tree116627.png)
* **This method returns false**
    
    The items are displayed via a combo box editor (in the list mode).
    
    ![SingleChoiceAction_List](~/images/singlechoiceaction_list116628.png)

> [!NOTE]
> The control used to display a Single Choice Action in the list or tree mode depends on the [SingleChoiceAction.ItemType](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.ItemType) property. To see how Single Choice Actions are displayed in different modes, see the **Actions** section in the **Feature Center Demo**, installed with XAF in the _[!include[PathToFeatureCenter](~/templates/path-to-feature-center.md)]_ folder, or refer to the [Feature Center demo online](https://demos.devexpress.com/XAF/featurecenter).
