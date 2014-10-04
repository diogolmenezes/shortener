Shortener = function(){
  this.trigger     = $('.btn');
  this.target      = $('#result');
  this.form        = $('form');
  this.action      = this.form.attr('action');
  this.fail_class  = 'fail';
}

Shortener.prototype.toShort = function(obj, e){
  e.preventDefault();

  context = this;

  $.post(this.action, this.form.serialize(), function(data){
    if(data.success)
    {
      context.target.html('<p>Parabéns. Sua URL é <a href="/' + data.short + '" title="' + data.original +'">http://localhost:8000/' + data.short + '</a></p>')
      context.target.removeClass(context.fail);
    }
    else
    {
      context.target.html('<p>Ops. Tente novamente.</p>');
      context.target.addClass(class_fail);
    }

    context.target.slideDown('slow');
  });

}

Shortener.apply = function(){
  shortener = new Shortener();
  shortener.trigger.on('click', function(e){ shortener.toShort(this, e); });
}
