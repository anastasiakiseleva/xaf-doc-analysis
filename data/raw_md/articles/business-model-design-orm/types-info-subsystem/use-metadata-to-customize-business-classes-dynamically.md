---
uid: "113583"
title: Use Metadata to Customize Business Classes Dynamically
seealso:
- linkId: "404195"
- linkId: "113179"
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-customize-xpo-business-model-at-runtime
  altText: 'GitHub Example: XAF - Customize an XPO Business Model at Runtime'
---
# Use Metadata to Customize Business Classes Dynamically

This topic describes how to manipulate business object metadata to alter an existing data model without the need to modify its code. This technique allows end users (application administrators) to add custom fields to business objects in the [Model Editor](xref:112582) so that there is no need to recompile the application. XAF application developers can also use this technique to add custom fields to objects implemented in external libraries where code is not available for modification. 

A custom field can be calculated (values are computed based on a specified expression) or persistent (values are saved in the data store). Use the table below to determine what types of custom fields are compatible with your business objects:

|                   | XPO | Entity Framework Core | Non-persistent objects |
|-------------------|:---:|:---------------------:|:----------------------:|
| Calculated fields | ✅ | ✅ |  |
| Persistent (editable) fields | ✅ |  | ✅ |

Custom fields declared in the Application Model are automatically collected and registered within the [Types Info](xref:113669) subsystem. Pay attention to the following specifics of runtime custom fields use:

* Generally, _persistent_ fields should be added at design time only. It is not good practice to allow end users to alter the database schema - allow this only as a last resort.
* It is strongly recommended to restart the application after a custom field is deleted at runtime.
* Custom fields added to the user differences (_Model.User.xafml_ file) are not supported when the [](xref:DevExpress.Xpo.ThreadSafeDataLayer) [Data Access Layer](xref:2123#data-access-layer) is in use. In XAF, this Data Layer is enabled when you instantiate an [](xref:DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider) using the constructor that takes the `threadSafe` parameter and set this parameter to `true`. The `SecuredObjectSpaceProvider` used in [Integrated Mode](xref:113436) of the Security System uses the `ThreadSafeDataLayer` by default, when the `threadSafe` parameter is not specified. As a workaround, copy a custom field to the administrator's differences (_Model.xafml_) by using the [Model Merge](xref:113334) feature.
* Calculated fields are always evaluated on the client side. So, sorting, grouping, filtering, and summary calculation do not work for calculated columns in [Server, ServerView, InstantFeedback, and InstantFeedbackView](xref:118450) modes. If you use XPO and create a new calculated field with one of the techniques described in this topic, the [](xref:DevExpress.Xpo.PersistentAliasAttribute) is automatically added to this newly created field. Thus, these operations are available for the corresponding column.
* You cannot add custom persistent fields to the EF Core data model.
* You can add custom persistent fields to a [non-persistent class](xref:116516) only if it inherits `NonPersistentBaseObject`. Note that these fields are not stored in a database. You can change them in the UI and get values in code as described in the [Access a Custom Field in Code](#access-a-custom-field-in-code) section.
* You cannot add custom [collection properties](xref:113568) to a [non-persistent class](xref:116516).

> [!NOTE]
> To see custom fields in action, refer to the **Custom Fields** section in the **Feature Center** demo installed with XAF. [!include[FeatureCenterLocationNote](~/templates/featurecenterlocationnote111102.md)]

## Add a Custom Calculated Field in the Model Editor
To add a custom calculated field, [invoke the Model Editor](xref:113326) at design time or in a WinForms application at runtime. Alternatively, use the standalone Model Editor. Then follow the steps below.

1. Right-click the **BOModel** | **_\<Class\>_** | **OwnMembers** node and choose **Add…** | **Member**.
	
	![AddCustomField_ME](~/images/addcustomfield_me117365.png)
2. Focus the new member node. In the property grid to the right, specify the [IModelMember.Name](xref:DevExpress.ExpressApp.Model.IModelMember.Name) and [IModelMember.Type](xref:DevExpress.ExpressApp.Model.IModelMember.Type) values.
3. Pass the expression to be used to compute the field value to the [IModelMember.Expression](xref:DevExpress.ExpressApp.Model.IModelMember.Expression) property. You can click the ellipsis button located to the right of the property value to invoke the [Expression Editor](xref:6212) dialog. In this editor, you can select functions, operators, and operands using editor controls.
4. If you are creating a custom field at runtime, specify the [IModelCommonMemberViewItem.PropertyEditorType](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.PropertyEditorType) value. Choose an appropriate Property Editor from the combo box. At design time, the **PropertyEditorType** value is optional - an appropriate Property Editor is determined automatically. Note that platform-specific Property Editors are not available in the common module.
5. Save your changes and restart the Model Editor.
6. Create a Detail View item or List View column mapped to the newly added custom field (see [](xref:403217) and [](xref:113679)).

The image below illustrates the member node settings described above.

![AddCustomField_ME2](~/images/addcustomfield_me2117366.png)

## Add a Custom Persistent Field in the Model Editor in Visual Studio
Creating a custom persistent field is very similar to creating the calculated field described in the previous section. The only difference is that you should set the [IModelMember.IsCalculated](xref:DevExpress.ExpressApp.Model.IModelMember.IsCalculated) property to `false` instead of specifying the `Expression` value.

> [!NOTE]
> [!include[ThreadSafe_CustomFields_Note](~/templates/threadsafe_customfields_note111210.md)]

## Add a Custom Persistent Field in the Model Editor at Runtime
The creation of custom persistent fields is allowed at design time only (the `IsCalculated` value is not editable). To allow end users to add custom persistent fields in the Model Editor at runtime, set the static [ModelMemberReadOnlyCalculator.AllowPersistentCustomProperties](xref:DevExpress.ExpressApp.Model.Core.ModelMemberReadOnlyCalculator.AllowPersistentCustomProperties) property to `true`. The created field should then be merged to the application-level model differences (see [Model Merge Tool](xref:113334)). To allow updating of the database schema after a field is added at runtime, set the [XafApplication.DatabaseUpdateMode](xref:DevExpress.ExpressApp.XafApplication.DatabaseUpdateMode) property to [DatabaseUpdateMode.UpdateDatabaseAlways](xref:DevExpress.ExpressApp.DatabaseUpdateMode.UpdateDatabaseAlways). Also, consider the note about `ThreadSafeDataLayer` from the [previous section](#add-a-custom-persistent-field-in-the-model-editor-in-visual-studio). A column mapped to the current field will automatically be added to the database table.

> [!IMPORTANT]
> * If you [store the Application Model Differences in the database](xref:113698), you should additionally override the `XafApplication.OnSetupComplete` protected virtual method and call the `XafApplication.CheckCompatibilityCore` method from the overridden method.
> * [!include[CustomFields_ServerAppNote](~/templates/customfields_serverappnote111922.md)]

## Add Custom Fields in Code
To extend an existing business class from an external class library, you can add a custom field in code. Edit the [!include[File_Module](~/templates/file_module11171.md)] file and override the [ModuleBase.CustomizeTypesInfo](xref:DevExpress.ExpressApp.ModuleBase.CustomizeTypesInfo(DevExpress.ExpressApp.DC.ITypesInfo)) method. The following code snippet adds a persistent field (`PersistentField1`), a persistent field with the [](xref:DevExpress.Persistent.Base.ImmediatePostDataAttribute) applied (`PersistentField2`), and a calculated field (`CalculatedField`).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.DC;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
// ...
public override void CustomizeTypesInfo(ITypesInfo typesInfo) {
    base.CustomizeTypesInfo(typesInfo);
    TypeInfo personTypeInfo = typesInfo.FindTypeInfo(typeof(Person)) as TypeInfo;
    if (personTypeInfo != null) {
        personTypeInfo.CreateMember("PersistentField1", typeof(int));
        personTypeInfo.CreateMember("PersistentField2", typeof(int)).AddAttribute(new ImmediatePostDataAttribute());
        personTypeInfo.CreateMember("CalculatedField", typeof(int), "PersistentField1 + PersistentField2");
    }
}
```

***

## Access a Custom Field in Code
The following snippet illustrates how to access a custom field in a [Controller](xref:112621) context using the [IMemberInfo.GetValue](xref:DevExpress.ExpressApp.DC.IMemberInfo.GetValue(System.Object)) method.

# [C#](#tab/tabid-csharp)

```csharp
Person person = this.View.CurrentObject as Person;
ITypeInfo personInfo = this.Application.TypesInfo.FindTypeInfo(typeof(Person));
int? value = personInfo.FindMember("CalculatedField").GetValue(person) as int?;
```

***

The following snippet illustrates how to access a custom field in a [Controller](xref:112621) context from the [PropertyEditor.ControlValue](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ControlValue) property.

# [C#](#tab/tabid-csharp)

```csharp
ViewItem viewItem = ((DetailView)View).FindItem("CalculatedField");
decimal? value = ((PropertyEditor)viewItem).ControlValue as decimal?;
```

***

## Create Associations in Code
The following snippet illustrates how to declare an association between two class properties when you have no access to the code of these classes and cannot apply the [](xref:DevExpress.Xpo.AssociationAttribute) directly.

# [C#](#tab/tabid-csharp)

```csharp
public override void CustomizeTypesInfo(ITypesInfo typesInfo) {
    base.CustomizeTypesInfo(typesInfo);
    ITypeInfo typeInfo1 = typesInfo.FindTypeInfo(typeof(DomainObject1));
    ITypeInfo typeInfo2 = typesInfo.FindTypeInfo(typeof(DomainObject2));
    IMemberInfo memberInfo1 = typeInfo1.FindMember("Object2");
    IMemberInfo memberInfo2 = typeInfo2.FindMember("Object1s");
    if(memberInfo1 == null) {
        memberInfo1 = typeInfo1.CreateMember("Object2", typeof(DomainObject2));
        memberInfo1.AddAttribute(new DevExpress.Xpo.AssociationAttribute("A", typeof(DomainObject2)), true);
    }
    if(memberInfo2 == null) {
        memberInfo2 = typeInfo2.CreateMember("Object1s", typeof(XPCollection<DomainObject1>));
        memberInfo2.AddAttribute(new DevExpress.Xpo.AssociationAttribute("A", typeof(DomainObject1)), true);
        memberInfo2.AddAttribute(new DevExpress.Xpo.AggregatedAttribute(), true);
    }
    ((XafMemberInfo)memberInfo1).Refresh();
    ((XafMemberInfo)memberInfo2).Refresh();
}
```

***

As you can see in the code above, the [IMemberInfo.AddAttribute](xref:DevExpress.ExpressApp.DC.IMemberInfo.AddAttribute(System.Attribute,System.Boolean)) method's second parameter is **true**. In this case, Types Info does not reload information from [](xref:DevExpress.Xpo.Metadata.XPDictionary) immediately. After adding all required attributes, call the **XafMemberInfo.Refresh** method for each updated member. Alternatively, you can call **XafTypesInfo.RefreshInfo** for each type containing updated members:

# [C#](#tab/tabid-csharp)

```csharp
public override void CustomizeTypesInfo(ITypesInfo typesInfo) {
    // ...
    typesInfo.RefreshInfo(typeof(DomainObject1));
    typesInfo.RefreshInfo(typeof(DomainObject2));
}
```

***

> [!TIP]
> To access the [](xref:DevExpress.Xpo.Metadata.XPDictionary) directly, use the [XpoTypesInfoHelper.GetXpoTypeInfoSource](xref:DevExpress.ExpressApp.Xpo.XpoTypesInfoHelper.GetXpoTypeInfoSource) method.