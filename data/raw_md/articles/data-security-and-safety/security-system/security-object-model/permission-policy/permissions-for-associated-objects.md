---
uid: "116170"
seealso: []
title: Permissions for Associated Objects
owner: Ekaterina Kiseleva
seealso:
- linkId: "113556"
---
# Permissions for Associated Objects

This topic explains how the [XAF Security System](xref:113366) processes permissions for [one-to-many associations](#permissions-for-one-to-many-associations), [many-to-many associations](#permissions-for-many-to-many-associations), and [reference properties](#permissions-for-reference-objects).  

## Permissions for One-to-Many Associations

The [Security System](xref:113366) automatically configures permissions for one side of an association if the other side is specified. You can also specify permissions for both sides of an association. For information on how to do that, refer to the following topic: [](xref:113556).

### Non-Aggregated Objects

The Security System allows users to read/write a [non-aggregated associated](xref:402958#one-to-many-non-aggregated) property if you explicitly granted access to one side of the association.

For example, the **Department** and **Contact** business objects form a one-to-many relationship. The **Department** type implements the **Contacts** collection property. When you grant access to **Department.Contacts**, the Security System allows access to the **Contact.Department** property. The Security System also allows access to the [default properties](xref:113525) of associated objects, unless the properties are marked with the [PersistentAlias](xref:DevExpress.Xpo.PersistentAliasAttribute) attribute. These properties are used to identify referenced objects in the application UI.

> [!IMPORTANT] 
> The **Contact** List View is displayed even if you did not allow access to this type explicitly. If such behavior is undesirable, manually prohibit access to the type.

### Aggregated Objects

If you specify a _read_ permission for an [aggregated](xref:402958#one-to-many-aggregated) collection and do not specify permissions for another side of an association, the Security System grants _read_ permissions for the aggregated type. If you specify a _write_ permission for the aggregated collection, the Security System allows _write_/_create_/_delete_ operations on the aggregated type.

For example, **Contact** and **Note** business objects form a one-to-many relationship. **Contact** implements the **Notes** aggregated collection property. If you grant permissions to read the **Contact.Notes** collection, the Security System automatically allows users to read the **Note** type. If you grant write permissions for the same collection, the Security System automatically allows users to create, edit, and delete **Note** objects.

> [!IMPORTANT] 
> In this example, a user can access the **Note** type and all its properties. If such behavior is undesirable, manually prohibit access to the type.

## Permissions for Many-to-Many Associations

The Security System requires explicitly specified permissions for both sides of a many-to-many association. See the following topic for information on how to manually specify required permissions: [](xref:113556).

## Permissions for Reference Objects

Read/write permissions for a reference property in the parent object apply to all members of the linked object (except for properties of secured types). Note that if read/write permissions for the reference object or some of its members are explicitly _prohibited_ by active security rules, these rules take precedence and override the automatically granted permissions.

For example, consider an **Order** business object that has a **FileData** reference property of the **FileData** type. Assume that you add permissions that allow users to read an **Order** object's **FileData** property. If automatic permissions for reference properties are enabled, users will be automatically granted permissions to read **FileData** objects that are linked to **Order** objects. Otherwise, you would need to [manually configure permissions for the FileData type](xref:113556).
> [!IMPORTANT] 
> In this example, a user can access the **FileData** type and all its properties. If such behavior is undesirable, manually prohibit access to the type.

[Template Kit](xref:405447) generates code that enables the described behavior in new projects. To enable it in projects created by older versions of the wizard, set the `SecurityStrategy.AutoAssociationReferencePropertyMode` setting to `AllMembers`.

**File:** _MySolution.Blazor.Server/Program.cs_, _MySolution.Win/Program.cs_, _MySolution.WebApi/Program.cs_

# [C#](#tab/tabid-csharp)

```csharp
public static int Main(string[] args) {
    // ...
    DevExpress.ExpressApp.Security.SecurityStrategy.AutoAssociationReferencePropertyMode = 
        DevExpress.ExpressApp.Security.ReferenceWithoutAssociationPermissionsMode.AllMembers;
}
```
***

To explicitly disable this behavior, set the `SecurityStrategy.AutoAssociationReferencePropertyMode` setting to `None`:

**File:** _MySolution.Blazor.Server/Program.cs_, _MySolution.Win/Program.cs_, _MySolution.WebApi/Program.cs_

# [C#](#tab/tabid-csharp)

```csharp
public static int Main(string[] args) {
    // ...
    DevExpress.ExpressApp.Security.SecurityStrategy.AutoAssociationReferencePropertyMode = 
        DevExpress.ExpressApp.Security.ReferenceWithoutAssociationPermissionsMode.None;
}
```
***

## Processing Modes for Associated Object Permissions

The [](xref:DevExpress.ExpressApp.Security.AssociationPermissionsMode) enumeration lists modes that determine how the Security System processes permissions for associated objects. To change the mode, set the [SecurityStrategy.AssociationPermissionsMode](xref:DevExpress.ExpressApp.Security.SecurityStrategy.AssociationPermissionsMode) property to one of the following values:

{|
|-

! Value
! Description
|-

| Auto
| The default mode. This mode does not process criteria in permissions for the 'Many' association's side but works faster than **ExtendedAuto**. If you have criteria in these permissions, set permissions on both sides of an association or use the **ExtendedAuto** mode.
|-

| ExtendedAuto
| This mode handles all scenarios but is slower than **Auto**. If this mode slows down your application, set permissions with criteria on both sides of the association.
|-

| Manual
| Use this mode to configure permissions for both sides of the association. Refer to the [How to: Manually Configure Permissions for Associated Collections and Reference Properties](xref:113556) topic for more information on this approach.
|}

## Permission Request Calculation Process

Use the [SecuritySystem.IsGranted](xref:DevExpress.ExpressApp.SecuritySystem.IsGranted*) method to check whether a member, a type, or an object has permissions that allow a user to execute or prevent a user from executing an operation.

### Check Permissions for a Member

1. The Security System makes a permission request for the specified member and checks _if this member is a part of an association_ (see [IMemberInfo.IsAssociation](xref:DevExpress.ExpressApp.DC.IMemberInfo.IsAssociation)). If this condition is satisfied, the **IsGranted** method returns one of the following values; otherwise, the Security System checks the next condition (step 2).
    * If the specified member has a permission that explicitly denies an operation (you set "Deny" for the operation), the **IsGranted** method returns **false**. 
    * If the specified member does not have a permission that explicitly denies an operation, the Security System makes a permission request for the associated member. The **IsGranted** method returns one of the values listed below:
        * **false** - if the associated member has a permission that explicitly denies the operation;
        * **true** - if the specified or associated member has a permission that explicitly allows the operation;
        * a value determined by the Permission Policy - if the associated member does not have any explicitly specified permissions.
        
    ![Check Permissions Chart1](~/images/PermissionsForAssociations_members_1.png)

2. If an association was not found at the first step, the Security System checks _if the member has explicitly specified permissions_. If this condition is satisfied, the **IsGranted** method returns one of the values listed below; otherwise, the Security System checks the next condition (step 3).
    * **false** - if the specified member has a permission that explicitly denies an operation (you set "Deny" for the operation); 
    * **true** - if the specified member has a permission that explicitly allows an operation.

    ![Check Permissions Chart2](~/images/PermissionsForAssociations_members_2.png)

3. If an association was not found at the first step and the member does not have explicitly specified permissions, the Security System checks _if the specified member is a default property_ (see <xref:DevExpress.ExpressApp.DC.XafDefaultPropertyAttribute>). If this condition is satisfied, the Security System makes a permission request for all associations in the class that contains this member; otherwise, it checks the next condition (step 4). The **IsGranted** method returns one of the values listed below:
    * **true** - if there is at least one association where this class participates and the type on the other side of the association has explicit permission for this operation;
    * a value determined by the Permission Policy - if no one association in this class has explicitly specified permissions.

    ![Check Permissions Chart3](~/images/PermissionsForAssociations_members_3.png)

4. If no condition in any previous step was met, the Security System checks_ if the class that implements this member is used in another class as a type of an aggregated collection_. The **IsGranted** method returns one of the values listed below:
    * **false** - if the aggregated collection has a permission that explicitly denies the operation;
    * **true** - if the aggregated collection has a permission that explicitly allows the operation;
    * a value determined by the Permission Policy - if the aggregated collection does not have explicitly specified permissions or the condition is not satisfied.

    ![Check Permissions Chart4](~/images/PermissionsForAssociations_members_4.png)

### Check Permissions for a Type or an Object

1. The Security System requests permission for the specified type. If a [Type Permission](xref:404633#type-permissions) is explicitly allowed/denied (you set "Allow"/"Deny" for the operation), the **IsGranted** method returns **true**/**false**.
2. If the Type Permission was not found at the previous step, the Security System checks if the specified type is used in another class as the type of an aggregated collection. If this condition is satisfied, the Security System makes a permission request for this collection. If the aggregated collection has a permission that explicitly allows/denies the operation, the **IsGranted** method returns **true**/**false**.
3. If the conditions listed above are not satisfied, the **IsGranted** method returns a value determined by the Permission Policy.

![PermissionsForAssociations_type](~/images/PermissionsForAssociations_type.png)

> [!NOTE] 
> The Security System does not process permission requests for the association's _Navigate_ operation.
