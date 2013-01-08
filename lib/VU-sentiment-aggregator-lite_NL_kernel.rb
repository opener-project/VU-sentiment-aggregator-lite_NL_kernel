module Opener
   module Kernel
     module VU
       module SentimentAggregator
    	 module Lite
    	   module NL
      		VERSION = "0.0.1"

      		class Configuration
        		CORE_DIR    = File.expand_path("../core", File.dirname(__FILE__))
        		KERNEL_CORE = CORE_DIR+'/SentimentAggregatorLite.py --no-time'
      		end

    	  end
    	end
      end
    end
  end
end

KERNEL_CORE=Opener::Kernel::VU::SentimentAggregator::Lite::NL::Configuration::KERNEL_CORE
