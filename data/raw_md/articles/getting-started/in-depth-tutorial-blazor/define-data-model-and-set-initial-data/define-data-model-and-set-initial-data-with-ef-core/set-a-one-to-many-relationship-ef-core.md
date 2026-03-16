---
uid: "402984"
title: Configure a One-to-Many Relationship
owner: Alexey Kazakov
seealso:
  - linkId: "112701"
  - linkId: "112654"
---
# Configure a One-to-Many Relationship

This lesson explains how to create a One-to-Many relationship between two entities and how XAF generates the UI for such a relationship.

> [!NOTE]
> Before you proceed, take a moment to review the previous lessons:
> 
> * [](xref:402981)
> * [](xref:404256)
> * [](xref:402985)

## Employee-Department Relationship

1. In the _MySolution.Module\Business Objects_ folder, create the `Department` class. Replace the generated class declaration with the following code:

    ```csharp
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl.EF;
    using System.ComponentModel;

    namespace MySolution.Module.BusinessObjects {
        [DefaultClassOptions]
        [DefaultProperty(nameof(Title))]
        public class Department : BaseObject {
            public virtual string Title { get; set; }
            public virtual string Office { get; set; }
        }
    }
    ```
    [`DefaultProperty`]: xref:System.ComponentModel.DefaultPropertyAttribute
    
    The code applies the `DefaultProperty` attribute to the `Department` class. Use this attribute to specify the most descriptive property of your class. [Default property](xref:113525) values are displayed in the following UI elements:
    
    * Detail form captions
    * The leftmost column of a List View
    * Lookup List Views

    Refer to the following topic for more information: [Data Annotations in Data Model](xref:112701).

2. Go to the _MySolution.Module\MySolutionDbContext_ file and add a DbSet of the `Department` class:

    ```csharp{3}
    public class MySolutionEFCoreDbContext : DbContext {
        //...
        public DbSet<Department> Departments { get; set; }
    }
    ```
    
3. Add the `Department` reference property to the `Employee` class:

    ```csharp
    //...
    public class Employee : BaseObject {
        //...
        public virtual Department Department { get; set; }
    }
    ```

    When you add a reference property of one entity type to another entity type, you establish the "One" part of the relationship between these entities. In this case it is a relationship between the `Department` and `Employee` entity classes.

    Note that the property has the `virtual` access modifier for lazy loading implementation. For additional information, refer to the Microsoft documentation: [Lazy Loading](https://learn.microsoft.com/en-us/ef/core/querying/related-data/lazy).

4. Add the `Employees` collection property to the `Department` class and initialize it in the constructor:
    
    ```csharp{2,6}
    // ...
    using System.Collections.ObjectModel;
    //...
    public class Department : BaseObject {
        //..
        public virtual IList<Employee> Employees { get; set; } = new ObservableCollection<Employee>();
    }
    ```

    This way, you implement the "Many" part of the relationship between the `Department` object and the `Employee` object.

5. Run the application. 

   Open the **Department** Detail View. You can see the **Employees** group. This is how XAF renders the `Employees` collection property.
   
   To add objects to the `Employees` collection, use the **New** or **Link** button in this tab. The **Link** button allows users to add references to existing `Employee` objects.

   ASP.NET Core Blazor
        
   :   ![|ASP.NET Core Blazor One-to-Many Relation Collection|](~/images/btutorial_bmd_lesson6.png)

   Windows Forms

   :   ![Windows Forms One-to-Many Relation Collection](~/images/department-employee-winforms.png)

       To remove a reference to an object from this collection, select this object and click **Unlink**.
    
       > [!TIP]
       > If you create a new `Department` and then create a new `Employee` in the `Employees` collection, the associated `Department` is not immediately visible in the [Detail View](xref:112611) of the newly created `Employee` object. The link between these objects is added later when you save the `Employee` object. To change this behavior, use the [XafApplication.LinkNewObjectToParentImmediately](xref:DevExpress.ExpressApp.XafApplication.LinkNewObjectToParentImmediately) property. When the property value is `true`, the application creates a link and saves it immediately after you click **New**.

6. Open the `Employee` Detail View. In this view, XAF creates a lookup editor for the `Department` reference property. Lookup editors support incremental filtering. This editor uses a special type of [View](xref:112611) --- Lookup List View. The Lookup List View includes a single column that displays the values of the default property. In your application, these are the values of the `Title` property.
   
   ASP.NET Core Blazor
        
   :   ![|ASP.NET Core Blazor One-to-Many Relation Reference|](~/images/tutorial-onetomany-reference-blazor.png)

   Windows Forms

   :   ![Windows Forms One-to-Many Relation Reference](~/images/tutorial-onetomany-reference-winforms.png)

> [!NOTE]
> The most common pattern for a relationship is to define properties on both ends of the relationship. At the same time, according to the conventions of Entity Framework Core, it is sufficient to add only the reference property (the "One" part). It establishes the "One-To-Many" relationship between entities and Entity Framework Core automatically creates a foreign key to the related table in the database.
>
> The main difference between these techniques is how XAF renders the application's UI. When you omit the "Many" part of the relationship, XAF doesn't create an editor for the omitted collection property in the Detail View of the entity class. You can see an example of this in the following lesson: [](xref:402978).

## Exercise: Create an Employee-PhoneNumber Relationship

1. Create a `PhoneNumber` class and implement a One-To-Many relationship between this class and the `Employee` class. This time the `Employee` should be the "One" part of the relationship, while the `PhoneNumber` should be the "Many" part. You can find the type declaration in the code sample below.

   > [!TIP]
   >
   > Remember to register the new entity in `DbContext`.
   
   Use the code sample below to replace the autogenerated class declaration in the `PhoneNumber` class:

   ```csharp
   using DevExpress.Persistent.BaseImpl.EF;
   using System.ComponentModel;

   namespace MySolution.Module.BusinessObjects;

   [DefaultProperty(nameof(Number))]
   public class PhoneNumber : BaseObject {
        public virtual String Number { get; set; }
        public virtual String PhoneType { get; set; }
        public override String ToString() {
            return Number;
        }
   }
   ```

   This class is not visible in the navigation control.

2. Run the application. Open the **Employee** Detail View to see the **Phone Numbers** group:

   ASP.NET Core Blazor

   :   ![|ASP.NET Core Blazor Employee-PhoneNumber relationship|](~/images/tutorial-employee-phonenumber-blazor.png)

   Windows Forms

   :   ![Windows Forms Employee-PhoneNumber relationship](~/images/tutorial-employee-phonenumber-winforms.png)

## Next Lesson

[](xref:402983)