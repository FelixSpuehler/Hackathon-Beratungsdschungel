function createForm() {
        
        // create & name Form
        var item = "Digitale Studienberatung";
        var form = FormApp.create(item).setTitle(item);
        // Page 1
        var Page1 = form.addPageBreakItem().setTitle("Herzlich Willkommen zur Online-Hausarbeitshilfe!");
        title = "Hast du ein genaues Thema?";
        var item = form.addMultipleChoiceItem();  
        item.setTitle(title).setChoices([item.createChoice('Ja', Page3), item.createChoice('Nein', Page4)]).setRequired(true);
        // Page 2
        var Page2 = form.addPageBreakItem().setTitle("Halt stop!").setHelpText("Hier solltest du nicht sein!").setGoToPage(FormApp.PageNavigationType.SUBMIT);
        // Page 3
        var Page3 = form.addPageBreakItem().setTitle("You're on a good way!").setHelpText("Prima.").setGoToPage(FormApp.PageNavigationType.SUBMIT);
        // Page 4
        var Page4 = form.addPageBreakItem().setTitle("You‘re on a bad way!").setHelpText("Schade.").setGoToPage(FormApp.PageNavigationType.SUBMIT);
        
}