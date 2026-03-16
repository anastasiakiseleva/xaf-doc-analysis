---
uid: DevExpress.ExpressApp.Model.IModelMember.IsCustom
name: IsCustom
type: Property
summary: Specifies whether the current property is [custom](xref:113583).
syntax:
  content: |-
    [ModelBrowsable(typeof(ModelMemberVisibilityCalculator))]
    bool IsCustom { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the property is custom; otherwise, **false**.'
seealso: []
---
Internally, custom properties are added using the [XPClassInfo.CreateMember](xref:DevExpress.Xpo.Metadata.XPClassInfo.CreateMember*) method.