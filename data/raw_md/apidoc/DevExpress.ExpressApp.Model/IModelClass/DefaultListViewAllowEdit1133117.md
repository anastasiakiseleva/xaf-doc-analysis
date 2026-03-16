---
uid: DevExpress.ExpressApp.Model.IModelClass.DefaultListViewAllowEdit
name: DefaultListViewAllowEdit
type: Property
summary: Specifies whether [in-place editing](xref:113249#in-place-editing) is allowed in List Views whose @DevExpress.ExpressApp.Model.IModelObjectView.ModelClass property is set to the corresponding **IModelClass** instance. This option does not affect lookup List Views.
syntax:
  content: |-
    [DefaultValue(false)]
    bool DefaultListViewAllowEdit { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true** to allow in-place editing; **false** to prohibit in-place editing.'
seealso:
- linkId: "113249"
---
To set this property, open the [Model Editor](xref:112582) and navigate to the **Application** | **BOModel** | _**\<Class>**_ node: 

![The DefaultListViewAllowEdit property in the Model Editor](~/images/ModelEditor_DefaultListViewAllowEdit.png)

You can also use the [DefaultListViewOptions](xref:DevExpress.ExpressApp.DefaultListViewOptionsAttribute) attribute to allow in-place editing in code (see [Data Annotations in Data Model](xref:112701)).