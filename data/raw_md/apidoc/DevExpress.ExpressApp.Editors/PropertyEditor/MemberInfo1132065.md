---
uid: DevExpress.ExpressApp.Editors.PropertyEditor.MemberInfo
name: MemberInfo
type: Property
summary: Provides access to the **IMemberInfo** object that contains information on the property represented by the current Property Editor.
syntax:
  content: public IMemberInfo MemberInfo { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.DC.IMemberInfo
    description: A **IMemberInfo** object providing full information on the property represented by the current Property Editor.
seealso: []
---
Use the following members of the object returned by this property to get information on the current Property Editor's property:

* Specify the bound property's value:
    
    **GetValue** and **SetValue**
* Common information on the bound property:
    
    **MemberType**, **IsReadOnly**, **IsStructField**, **IsPersistent**, **IsKey**, **IsAggregated** and **Name**
* Information specified for the bound property in the Application Model:
    
    **FindAttribute**