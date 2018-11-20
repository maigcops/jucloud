var jucloud = { 
    "initSideMenu": function(hrefvalue, level=1) {
        if(level==2){
          linkMenu=$(".cloudmenu[href='"+hrefvalue+"']")
          parentMenu=linkMenu.parent().parent().siblings("a")
          parentMenu.addClass("active subdrop")
          linkMenu.closest('li').addClass("active")
          linkMenu.closest('ul').css("display", "block")
        }else{
          $(".cloudmenu[href='"+hrefvalue+"']").addClass("active")
        }
    }
}